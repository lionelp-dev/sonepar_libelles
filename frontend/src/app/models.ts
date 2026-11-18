export interface AuditHabilitations {
  id: number;
  created_at: string;
  habilitations_count: number;
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
