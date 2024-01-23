from sqlglot import parse_one, exp

# print all column references (a and b)
comments=parse_one('''CREATE TABLE 
    gbi_rdb_table_setting 
    ( 
        id bigint NOT NULL AUTO_INCREMENT COMMENT 'ID', 
        datax_job_json json COMMENT 'datax任务', 
        job_id VARCHAR(128) COMMENT 'job id', 
        status VARCHAR(32) COMMENT 'status', 
        access TINYINT(1) DEFAULT 0 COMMENT 'access', 
        column_setting json COMMENT 'table columns', 
        created_at    DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '创建时间', 
        created_user  VARCHAR(128) NOT NULL COMMENT '创建用户', 
        DATABASE      VARCHAR(128) NOT NULL COMMENT 'database', 
        datasource_id bigint NOT NULL COMMENT 'datasource ID', 
        project_id    VARCHAR(64) NOT NULL COMMENT 'project id', 
        TABLE         VARCHAR(128) NOT NULL COMMENT 'table', 
        table_setting json COMMENT 'table base info', 
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON 
UPDATE 
    CURRENT_TIMESTAMP NOT NULL COMMENT '最后更新的时间', 
    updated_user VARCHAR(128) NOT NULL COMMENT '最后更新的用户', 
    uri          VARCHAR(128) NOT NULL COMMENT 'uri', 
    version      INT(10) UNSIGNED DEFAULT 0 NOT NULL COMMENT 'version', 
    PRIMARY KEY (id) 
    ) 
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE=utf8mb4_general_ci COMMENT 'dsadsadsa';''').find_all(exp.Comment)
for comment in comments:
    print(comment)

# # find all projections in select statements (a and c)
# for select in parse_one("SELECT a, b + 1 AS c FROM d").find_all(exp.Select):
#     for projection in select.expressions:
#         print(projection.alias_or_name)
#
# # find all tables (x, y, z)
# for table in parse_one("SELECT * FROM x JOIN y JOIN z").find_all(exp.Table):
#     print(table.name)