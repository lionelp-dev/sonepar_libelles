export type ModelRecord = Record<string, string | number | boolean | null>;

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
