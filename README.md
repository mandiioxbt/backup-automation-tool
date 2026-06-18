# Backup Automation Tool

Automated backup with encryption, compression, and S3 upload.

## Features
- Incremental backups with deduplication
- AES-256-GCM encryption
- Multi-cloud: S3, GCS, Azure Blob
- Scheduled via cron or systemd timer

## CLI
```bash
backup run --source /data --dest s3://bucket/ --encrypt --incremental
backup verify --job-id latest --sample 10%
```

## License
MIT
