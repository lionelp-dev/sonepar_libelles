import csv
from io import StringIO

from django.test import TestCase
from rest_framework.test import APIClient

from .models import (
    AuditHabilitations,
    Habilitations,
    LibellesFonctions,
    LibellesNiveauxAcces,
    LibellesOptions,
    MNS150MI_LstUsers,
    MNS405MI_Lst,
    MNS410MI_LstRolesByUser,
    SES400MI_LstAuthByRole,
)


class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def create_source_data(self):
        MNS150MI_LstUsers.objects.create(
            user_id="DUPONTJ",
            nom_complet="Jeanne Dupont",
            statut="ACTIF",
        )
        MNS405MI_Lst.objects.create(
            role_id="ACHETEUR",
            nom_role="Acheteur",
            description="Rôle de test",
        )
        MNS410MI_LstRolesByUser.objects.create(user_id="DUPONTJ", role_id="ACHETEUR")
        SES400MI_LstAuthByRole.objects.create(
            role_id="ACHETEUR",
            code_fonction="PPS200",
            libelle_fonction="Article",
            societe="100",
            division="A01",
            statut="ACTIF",
            options_autorisees="1",
            niveau_acces=2,
        )
        LibellesFonctions.objects.create(
            code_fonction="PPS200",
            libelle_fonction="Gestion des articles",
            description="Libellé de test",
        )
        LibellesNiveauxAcces.objects.create(
            niveau_acces=2,
            libelle_niveau_acces="Modification autorisée",
            description="Niveau de test",
        )
        LibellesOptions.objects.create(
            code_option=1,
            libelle_option="Option standard",
            libelle_anglais="Standard option",
            description="Option de test",
        )

    def test_all_model_collections_are_available(self):
        self.create_source_data()
        audit = AuditHabilitations.objects.create()
        Habilitations.objects.create(
            audit=audit,
            user_id="DUPONTJ",
            nom_complet="Jeanne Dupont",
            role_id="ACHETEUR",
            nom_role="Acheteur",
            code_fonction="PPS200",
            libelle_fonction="Gestion des articles",
            societe="100",
            division="A01",
            statut="ACTIF",
            options_autorisees="1",
            libelles_options_autorisees="Option standard",
            niveau_acces=2,
            libelle_niveau_acces="Modification autorisée",
        )

        for endpoint in (
            "/api/users/",
            "/api/roles/",
            "/api/user-role-assignments/",
            "/api/role-authorizations/",
            "/api/function-labels/",
            "/api/access-levels/",
            "/api/options/",
            "/api/audits/",
            "/api/habilitations/",
        ):
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.json(), list)
                self.assertEqual(len(response.json()), 1)

    def test_post_audits_generates_enriched_habilitations(self):
        self.create_source_data()

        response = self.client.post("/api/audits/", data={}, format="json")

        self.assertEqual(response.status_code, 201)
        payload = response.json()
        self.assertEqual(payload["habilitations_count"], 1)
        habilitation = Habilitations.objects.get(audit_id=payload["id"])
        self.assertEqual(habilitation.nom_complet, "Jeanne Dupont")
        self.assertEqual(habilitation.libelle_fonction, "Gestion des articles")
        self.assertEqual(habilitation.libelles_options_autorisees, "Option standard")

    def test_post_audits_without_source_data_creates_an_empty_snapshot(self):
        response = self.client.post("/api/audits/", data={}, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["habilitations_count"], 0)
        self.assertEqual(AuditHabilitations.objects.count(), 1)

    def test_export_returns_csv_for_selected_audit(self):
        self.create_source_data()
        audit_response = self.client.post("/api/audits/", data={}, format="json")
        audit_id = audit_response.json()["id"]

        response = self.client.get(f"/api/audits/{audit_id}/export/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv; charset=utf-8")
        self.assertIn(
            f'audit_habilitations_{audit_id}_',
            response["Content-Disposition"],
        )
        self.assertIn("attachment;", response["Content-Disposition"])
        rows = list(csv.reader(StringIO(response.content.decode("utf-8-sig")), delimiter=";"))
        self.assertEqual(rows[0][0], "user_id")
        self.assertEqual(rows[1][0], "DUPONTJ")

    def test_export_of_unknown_audit_returns_404(self):
        response = self.client.get("/api/audits/999/export/")

        self.assertEqual(response.status_code, 404)
