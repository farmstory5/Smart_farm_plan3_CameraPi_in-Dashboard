from _typeshed import Incomplete
from typing import Any, overload
from typing_extensions import Literal

import sqlalchemy.types as sqltypes

from ...engine import default
from ...sql import compiler
from ...sql.elements import Cast
from ...types import (
    BIGINT as BIGINT,
    BINARY as BINARY,
    CHAR as CHAR,
    DATE as DATE,
    DATETIME as DATETIME,
    DECIMAL as DECIMAL,
    FLOAT as FLOAT,
    INTEGER as INTEGER,
    NCHAR as NCHAR,
    NUMERIC as NUMERIC,
    NVARCHAR as NVARCHAR,
    SMALLINT as SMALLINT,
    TEXT as TEXT,
    VARCHAR as VARCHAR,
)
from .json import JSON as JSON

MS_2017_VERSION: Any
MS_2016_VERSION: Any
MS_2014_VERSION: Any
MS_2012_VERSION: Any
MS_2008_VERSION: Any
MS_2005_VERSION: Any
MS_2000_VERSION: Any
RESERVED_WORDS: Any

class REAL(sqltypes.REAL):
    __visit_name__: str
    def __init__(self, **kw) -> None: ...

class TINYINT(sqltypes.Integer):
    __visit_name__: str

class _MSDate(sqltypes.Date):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class TIME(sqltypes.TIME):
    precision: Any
    def __init__(self, precision: Incomplete | None = None, **kwargs) -> None: ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

_MSTime = TIME

class _BASETIMEIMPL(TIME):
    __visit_name__: str

class _DateTimeBase:
    def bind_processor(self, dialect): ...

class _MSDateTime(_DateTimeBase, sqltypes.DateTime): ...

class SMALLDATETIME(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str

class DATETIME2(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str
    precision: Any
    def __init__(self, precision: Incomplete | None = None, **kw) -> None: ...

class DATETIMEOFFSET(_DateTimeBase, sqltypes.DateTime):
    __visit_name__: str
    precision: Any
    def __init__(self, precision: Incomplete | None = None, **kw) -> None: ...

class _UnicodeLiteral:
    def literal_processor(self, dialect): ...

class _MSUnicode(_UnicodeLiteral, sqltypes.Unicode): ...
class _MSUnicodeText(_UnicodeLiteral, sqltypes.UnicodeText): ...

class TIMESTAMP(sqltypes._Binary):
    __visit_name__: str
    length: Any
    convert_int: Any
    def __init__(self, convert_int: bool = False) -> None: ...
    def result_processor(self, dialect, coltype): ...

class ROWVERSION(TIMESTAMP):
    __visit_name__: str

class NTEXT(sqltypes.UnicodeText):
    __visit_name__: str

class VARBINARY(sqltypes.VARBINARY, sqltypes.LargeBinary):
    __visit_name__: str
    filestream: bool
    @overload
    def __init__(self, length: Literal["max"] | None, filestream: Literal[True]) -> None: ...
    @overload
    def __init__(self, *, filestream: Literal[True]) -> None: ...
    @overload
    def __init__(self, length: Incomplete | None = None, filestream: Literal[False] = False) -> None: ...

class IMAGE(sqltypes.LargeBinary):
    __visit_name__: str

class XML(sqltypes.Text):
    __visit_name__: str

class BIT(sqltypes.Boolean):
    __visit_name__: str

class MONEY(sqltypes.TypeEngine):
    __visit_name__: str

class SMALLMONEY(sqltypes.TypeEngine):
    __visit_name__: str

class UNIQUEIDENTIFIER(sqltypes.TypeEngine):
    __visit_name__: str

class SQL_VARIANT(sqltypes.TypeEngine):
    __visit_name__: str

class TryCast(Cast):
    __visit_name__: str
    stringify_dialect: str
    inherit_cache: bool
    def __init__(self, *arg, **kw) -> None: ...

try_cast: Any
MSDateTime: Any
MSDate: Any
MSReal = REAL
MSTinyInteger = TINYINT
MSTime = TIME
MSSmallDateTime = SMALLDATETIME
MSDateTime2 = DATETIME2
MSDateTimeOffset = DATETIMEOFFSET
MSText = TEXT
MSNText = NTEXT
MSString = VARCHAR
MSNVarchar = NVARCHAR
MSChar = CHAR
MSNChar = NCHAR
MSBinary = BINARY
MSVarBinary = VARBINARY
MSImage = IMAGE
MSBit = BIT
MSMoney = MONEY
MSSmallMoney = SMALLMONEY
MSUniqueIdentifier = UNIQUEIDENTIFIER
MSVariant = SQL_VARIANT
ischema_names: Any

class MSTypeCompiler(compiler.GenericTypeCompiler):
    def visit_FLOAT(self, type_, **kw): ...
    def visit_TINYINT(self, type_, **kw): ...
    def visit_TIME(self, type_, **kw): ...
    def visit_TIMESTAMP(self, type_, **kw): ...
    def visit_ROWVERSION(self, type_, **kw): ...
    def visit_datetime(self, type_, **kw): ...
    def visit_DATETIMEOFFSET(self, type_, **kw): ...
    def visit_DATETIME2(self, type_, **kw): ...
    def visit_SMALLDATETIME(self, type_, **kw): ...
    def visit_unicode(self, type_, **kw): ...
    def visit_text(self, type_, **kw): ...
    def visit_unicode_text(self, type_, **kw): ...
    def visit_NTEXT(self, type_, **kw): ...
    def visit_TEXT(self, type_, **kw): ...
    def visit_VARCHAR(self, type_, **kw): ...
    def visit_CHAR(self, type_, **kw): ...
    def visit_NCHAR(self, type_, **kw): ...
    def visit_NVARCHAR(self, type_, **kw): ...
    def visit_date(self, type_, **kw): ...
    def visit__BASETIMEIMPL(self, type_, **kw): ...
    def visit_time(self, type_, **kw): ...
    def visit_large_binary(self, type_, **kw): ...
    def visit_IMAGE(self, type_, **kw): ...
    def visit_XML(self, type_, **kw): ...
    def visit_VARBINARY(self, type_, **kw): ...
    def visit_boolean(self, type_, **kw): ...
    def visit_BIT(self, type_, **kw): ...
    def visit_JSON(self, type_, **kw): ...
    def visit_MONEY(self, type_, **kw): ...
    def visit_SMALLMONEY(self, type_, **kw): ...
    def visit_UNIQUEIDENTIFIER(self, type_, **kw): ...
    def visit_SQL_VARIANT(self, type_, **kw): ...

class MSExecutionContext(default.DefaultExecutionContext):
    def pre_exec(self) -> None: ...
    cursor_fetch_strategy: Any
    def post_exec(self) -> None: ...
    def get_lastrowid(self): ...
    @property
    def rowcount(self): ...
    def handle_dbapi_exception(self, e) -> None: ...
    def get_result_cursor_strategy(self, result): ...
    def fire_sequence(self, seq, type_): ...
    def get_insert_default(self, column): ...

class MSSQLCompiler(compiler.SQLCompiler):
    returning_precedes_values: bool
    extract_map: Any
    tablealiases: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def visit_now_func(self, fn, **kw): ...
    def visit_current_date_func(self, fn, **kw): ...
    def visit_length_func(self, fn, **kw): ...
    def visit_char_length_func(self, fn, **kw): ...
    def visit_concat_op_binary(self, binary, operator, **kw): ...
    def visit_true(self, expr, **kw): ...
    def visit_false(self, expr, **kw): ...
    def visit_match_op_binary(self, binary, operator, **kw): ...
    def get_select_precolumns(self, select, **kw): ...
    def get_from_hint_text(self, table, text): ...
    def get_crud_hint_text(self, table, text): ...
    def fetch_clause(self, cs, **kwargs): ...
    def limit_clause(self, cs, **kwargs): ...
    def visit_try_cast(self, element, **kw): ...
    def translate_select_structure(self, select_stmt, **kwargs): ...
    def visit_table(self, table, mssql_aliased: bool = ..., iscrud: bool = ..., **kwargs): ...  # type: ignore[override]
    def visit_alias(self, alias, **kw): ...
    def visit_column(self, column, add_to_result_map: Incomplete | None = ..., **kw): ...  # type: ignore[override]
    def visit_extract(self, extract, **kw): ...
    def visit_savepoint(self, savepoint_stmt): ...
    def visit_rollback_to_savepoint(self, savepoint_stmt): ...
    def visit_binary(self, binary, **kwargs): ...
    def returning_clause(self, stmt, returning_cols): ...
    def get_cte_preamble(self, recursive): ...
    def label_select_column(self, select, column, asfrom): ...
    def for_update_clause(self, select, **kw): ...
    def order_by_clause(self, select, **kw): ...
    def update_from_clause(self, update_stmt, from_table, extra_froms, from_hints, **kw): ...
    def delete_table_clause(self, delete_stmt, from_table, extra_froms): ...
    def delete_extra_from_clause(self, delete_stmt, from_table, extra_froms, from_hints, **kw): ...
    def visit_empty_set_expr(self, type_): ...
    def visit_is_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_is_not_distinct_from_binary(self, binary, operator, **kw): ...
    def visit_json_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_json_path_getitem_op_binary(self, binary, operator, **kw): ...
    def visit_sequence(self, seq, **kw): ...

class MSSQLStrictCompiler(MSSQLCompiler):
    ansi_bind_rules: bool
    def visit_in_op_binary(self, binary, operator, **kw): ...
    def visit_not_in_op_binary(self, binary, operator, **kw): ...
    def render_literal_value(self, value, type_): ...

class MSDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kwargs): ...
    def visit_create_index(self, create, include_schema: bool = False): ...  # type: ignore[override]
    def visit_drop_index(self, drop): ...
    def visit_primary_key_constraint(self, constraint): ...
    def visit_unique_constraint(self, constraint): ...
    def visit_computed_column(self, generated): ...
    def visit_create_sequence(self, create, **kw): ...
    def visit_identity_column(self, identity, **kw): ...

class MSIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any
    def __init__(self, dialect) -> None: ...
    def quote_schema(self, schema, force: Incomplete | None = None): ...

class MSDialect(default.DefaultDialect):
    name: str
    supports_statement_cache: bool
    supports_default_values: bool
    supports_empty_insert: bool
    use_scope_identity: bool
    max_identifier_length: int
    schema_name: str
    implicit_returning: bool
    full_returning: bool
    colspecs: Any
    engine_config_types: Any
    ischema_names: Any
    supports_sequences: bool
    sequences_optional: bool
    default_sequence_base: int
    supports_native_boolean: bool
    non_native_boolean_check_constraint: bool
    supports_unicode_binds: bool
    postfetch_lastrowid: bool
    legacy_schema_aliasing: bool
    server_version_info: Any
    statement_compiler: Any
    ddl_compiler: Any
    type_compiler: Any
    preparer: Any
    construct_arguments: Any
    query_timeout: Any
    deprecate_large_types: Any
    isolation_level: Any
    def __init__(
        self,
        query_timeout: Incomplete | None = None,
        use_scope_identity: bool = True,
        schema_name: str = "dbo",
        isolation_level: Incomplete | None = None,
        deprecate_large_types: Incomplete | None = None,
        json_serializer: Incomplete | None = None,
        json_deserializer: Incomplete | None = None,
        legacy_schema_aliasing: Incomplete | None = None,
        ignore_no_transaction_on_rollback: bool = False,
        **opts,
    ) -> None: ...
    def do_savepoint(self, connection, name) -> None: ...
    def do_release_savepoint(self, connection, name) -> None: ...
    def set_isolation_level(self, connection, level) -> None: ...
    def get_isolation_level(self, dbapi_connection): ...
    def initialize(self, connection) -> None: ...
    def on_connect(self): ...
    def has_table(self, connection, tablename, dbname, owner, schema): ...
    def has_sequence(self, connection, sequencename, dbname, owner, schema): ...
    def get_sequence_names(self, connection, dbname, owner, schema, **kw): ...
    def get_schema_names(self, connection, **kw): ...
    def get_table_names(self, connection, dbname, owner, schema, **kw): ...
    def get_view_names(self, connection, dbname, owner, schema, **kw): ...
    def get_indexes(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_view_definition(self, connection, viewname, dbname, owner, schema, **kw): ...
    def get_columns(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_pk_constraint(self, connection, tablename, dbname, owner, schema, **kw): ...
    def get_foreign_keys(self, connection, tablename, dbname, owner, schema, **kw): ...
