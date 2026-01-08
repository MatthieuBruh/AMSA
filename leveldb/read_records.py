import ccl_leveldb as ccl_leveldb

leveldb_path = 'fcm_queued_messages.ldb'
leveldb_records = ccl_leveldb.RawLevelDb(leveldb_path)

for record in leveldb_records.iterate_records_raw():
    print(record.seq, record.user_key, record.value)