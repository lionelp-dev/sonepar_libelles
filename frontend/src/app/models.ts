export interface AuditHabilitations {
  id: number;
  created_at: string;
  habilitations_count: number;
}

export interface Habilitation {
  id: number;
  audit: number;
  user_id: string;
  nom_complet: string;
  role_id: string;
  nom_role: string;
  code_fonction: string;
  libelle_fonction: string;
  societe: string;
  division: string;
  statut: string;
  options_autorisees: string;
  libelles_options_autorisees: string;
  niveau_acces: number;
  libelle_niveau_acces: string;
}

export type ModelRecord = Record<string, string | number | null>;

export interface ModelTableColumn {
  key: string;
  label: string;
}

export interface ModelDefinition {
  apiPath: string;
  title: string;
  description: string;
  columns: ModelTableColumn[];
}
