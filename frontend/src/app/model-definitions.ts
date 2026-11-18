import { ModelDefinition } from './models';

export type ReadOnlyModelName =
  | 'MNS150MI_LstUsers'
  | 'MNS405MI_Lst'
  | 'MNS410MI_LstRolesByUser'
  | 'SES400MI_LstAuthByRole'
  | 'LibellesFonctions'
  | 'LibellesNiveauxAcces'
  | 'LibellesOptions'
  | 'Habilitations';

export const modelDefinitions: Record<ReadOnlyModelName, ModelDefinition> = {
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
    description: 'Droits de fonctions retournés par SES400MI.',
    columns: [
      { key: 'role_id', label: 'Rôle' },
      { key: 'code_fonction', label: 'Fonction' },
      { key: 'libelle_fonction', label: 'Libellé source' },
      { key: 'societe', label: 'Société' },
      { key: 'division', label: 'Division' },
      { key: 'statut', label: 'Statut' },
      { key: 'options_autorisees', label: 'Options' },
      { key: 'niveau_acces', label: 'Niveau' },
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
  LibellesNiveauxAcces: {
    apiPath: 'access-levels/',
    title: 'LibellesNiveauxAcces',
    description: 'Référentiel des niveaux de droit.',
    columns: [
      { key: 'niveau_acces', label: 'Niveau' },
      { key: 'libelle_niveau_acces', label: 'Libellé' },
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
  Habilitations: {
    apiPath: 'habilitations/',
    title: 'Habilitations',
    description: 'Lignes enrichies, conservées dans les instantanés d’audit.',
    columns: [
      { key: 'audit', label: 'Audit' },
      { key: 'user_id', label: 'Utilisateur' },
      { key: 'nom_complet', label: 'Nom complet' },
      { key: 'role_id', label: 'Rôle' },
      { key: 'nom_role', label: 'Nom du rôle' },
      { key: 'code_fonction', label: 'Fonction' },
      { key: 'libelle_fonction', label: 'Libellé fonction' },
      { key: 'societe', label: 'Société' },
      { key: 'division', label: 'Division' },
      { key: 'statut', label: 'Statut' },
      { key: 'options_autorisees', label: 'Options' },
      { key: 'libelles_options_autorisees', label: 'Libellés des options' },
      { key: 'niveau_acces', label: 'Niveau' },
      { key: 'libelle_niveau_acces', label: 'Libellé niveau' },
    ],
  },
};
