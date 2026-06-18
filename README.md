# Backup Automation Tool

Automated backup with AES-256-GCM encryption, compression, and cloud upload.

## Features
- Incremental backups with deduplication
- Multi-cloud: S3, GCS, Azure Blob
- AES-256-GCM encryption at rest
- Scheduled via cron or systemd

## CLI
```bash
backup run --source /data --dest s3://bucket/ --encrypt --incremental
```

## License: Apache 2.0
