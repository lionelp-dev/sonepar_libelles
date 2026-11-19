import { ModelDefinition } from './models';

export type ReadOnlyModelName =
  | 'MNS110MI_Lst'
  | 'MNS150MI_LstUsers'
  | 'MNS405MI_Lst'
  | 'MNS410MI_LstRolesByUser'
  | 'SES400MI_LstAuthByRole'
  | 'SES401_CMNPUS'
  | 'SES510MI_Lst'
  | 'LibellesFonctions'
  | 'LibellesOptions';

export const modelDefinitions: Record<ReadOnlyModelName, ModelDefinition> = {
  MNS110MI_Lst: {
    apiPath: 'function-catalog/',
    title: 'MNS110MI_Lst',
    description: 'Catalogue des fonctions M3 retourné par MNS110MI.',
    columns: [
      { key: 'code_fonction', label: 'Code fonction' },
      { key: 'programme_m3', label: 'Programme M3' },
      { key: 'categorie_fonction', label: 'Catégorie' },
      { key: 'autorisation_requise', label: 'Autorisation requise' },
    ],
  },
  MNS150MI_LstUsers: {
    apiPath: 'users/',
    title: 'MNS150MI_LstUsers',
    description: 'Utilisateurs chargés depuis la transaction MNS150MI.',
    columns: [
      { key: 'user_id', label: 'Identifiant' },
      { key: 'nom_complet', label: 'Nom complet' },
      { key: 'statut', label: 'Statut' },
    ],
  },
  MNS405MI_Lst: {
    apiPath: 'roles/',
    title: 'MNS405MI_Lst',
    description: 'Rôles disponibles depuis la transaction MNS405MI.',
    columns: [
      { key: 'role_id', label: 'Identifiant' },
      { key: 'nom_role', label: 'Nom du rôle' },
      { key: 'description', label: 'Description' },
    ],
  },
  MNS410MI_LstRolesByUser: {
    apiPath: 'user-role-assignments/',
    title: 'MNS410MI_LstRolesByUser',
    description: 'Associations retournées par MNS410MI.',
    columns: [
      { key: 'user_id', label: 'Utilisateur' },
      { key: 'role_id', label: 'Rôle' },
    ],
  },
  SES400MI_LstAuthByRole: {
    apiPath: 'role-authorizations/',
    title: 'SES400MI_LstAuthByRole',
    description: 'Droits théoriques par rôle retournés par SES400MI.',
    columns: [
      { key: 'role_id', label: 'Rôle' },
      { key: 'code_fonction', label: 'Fonction' },
      { key: 'libelle_fonction', label: 'Libellé source' },
      { key: 'societe', label: 'Société' },
      { key: 'division', label: 'Division' },
      { key: 'statut', label: 'Statut' },
      { key: 'code_option', label: 'Code option' },
    ],
  },
  SES401_CMNPUS: {
    apiPath: 'user-authorizations/',
    title: 'SES401_CMNPUS',
    description: 'Droits effectifs par utilisateur retournés par SES401.',
    columns: [
      { key: 'user_id', label: 'Utilisateur' },
      { key: 'nom_complet', label: 'Nom complet' },
      { key: 'programme_m3', label: 'Programme M3' },
      { key: 'societe', label: 'Société' },
      { key: 'division', label: 'Division' },
      { key: 'role_id', label: 'Rôle' },
      { key: 'code_option', label: 'Code option' },
    ],
  },
  SES510MI_Lst: {
    apiPath: 'authorization-history/',
    title: 'SES510MI_Lst',
    description: 'Journal des modifications d’habilitations retourné par SES510MI.',
    columns: [
      { key: 'id_evenement', label: 'Événement' },
      { key: 'trdt', label: 'Date' },
      { key: 'trtm', label: 'Heure' },
      { key: 'usiu', label: 'Utilisateur source' },
      { key: 'conu', label: 'Société' },
      { key: 'divu', label: 'Division' },
      { key: 'prgnu', label: 'Programme' },
      { key: 'modifie_par', label: 'Modifié par' },
      { key: 'programme_origine', label: 'Programme origine' },
      { key: 'code_operation', label: 'Opération' },
      { key: 'role_modifie', label: 'Rôle modifié' },
      { key: 'fonction_modifiee', label: 'Fonction modifiée' },
      { key: 'utilisateur_modifie', label: 'Utilisateur modifié' },
      { key: 'code_option', label: 'Code option' },
      { key: 'autorisee_avant', label: 'Autorisée avant' },
      { key: 'autorisee_apres', label: 'Autorisée après' },
      { key: 'options_de_base_modifiees', label: 'Options de base modifiées' },
      { key: 'options_associees_modifiees', label: 'Options associées modifiées' },
      { key: 'touches_fonction_modifiees', label: 'Touches fonction modifiées' },
    ],
  },
  LibellesFonctions: {
    apiPath: 'function-labels/',
    title: 'LibellesFonctions',
    description: 'Référentiel des fonctions M3.',
    columns: [
      { key: 'code_fonction', label: 'Code fonction' },
      { key: 'libelle_fonction', label: 'Libellé' },
      { key: 'description', label: 'Description' },
    ],
  },
  LibellesOptions: {
    apiPath: 'options/',
    title: 'LibellesOptions',
    description: 'Référentiel des options M3.',
    columns: [
      { key: 'code_option', label: 'Code option' },
      { key: 'libelle_option', label: 'Libellé' },
      { key: 'libelle_anglais', label: 'Libellé anglais' },
      { key: 'description', label: 'Description' },
    ],
  },
};
