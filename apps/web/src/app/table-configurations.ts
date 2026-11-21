import { DatabaseTableName, TableConfiguration } from './tables';

export const tableConfigurations: Record<DatabaseTableName, TableConfiguration> = {
  ses510mi_lst: {
    apiPath: 'ses510mi/',
    tableName: 'ses510mi_lst',
    title: 'Journal d’audit de sécurité',
    subtitle: 'Données SES510MI enrichies avec des libellés',
    columns: [
      { key: 'trdt', label: 'trdt' }, { key: 'trtm', label: 'trtm' },
      { key: 'usiu', label: 'usiu' }, { key: 'conu', label: 'conu' }, { key: 'divu', label: 'divu' },
      { key: 'prgnu', label: 'prgnu' }, { key: 'libelle_prgnu', label: 'libelle_prgnu' }, { key: 'changed_by', label: 'changed_by' },
      { key: 'trans_program', label: 'trans_program' }, { key: 'libelle_trans_program', label: 'libelle_trans_program' }, { key: 'op_code', label: 'op_code' }, { key: 'libelle_op_code', label: 'libelle_op_code' },
      { key: 'changed_role', label: 'changed_role' }, { key: 'libelle_changed_role', label: 'libelle_changed_role' }, { key: 'changed_fnc', label: 'changed_fnc' }, { key: 'libelle_changed_fnc', label: 'libelle_changed_fnc' },
      { key: 'changed_user', label: 'changed_user' },
      { key: 'type_droit', label: 'type_droit' }, { key: 'code_option', label: 'code_option' }, { key: 'libelle_option', label: 'libelle_option' },
      { key: 'autorisee_avant', label: 'autorisee_avant' }, { key: 'autorisee_apres', label: 'autorisee_apres' },
    ],
  },
};
