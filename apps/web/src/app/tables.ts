export type TableRecord = Record<string, string | number | boolean | null>;

export interface TableColumn {
  key: string;
  label: string;
}

export interface TableConfiguration {
  apiPath: string;
  tableName: DatabaseTableName;
  title: string;
  subtitle: string;
  columns: TableColumn[];
}

export type DatabaseTableName =
  'ses510mi_lst';
