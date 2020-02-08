# Introduction
A python application that will update DNS of your domains on Cloudflare dynamically. It's already built as Docker image and ready to use. There's no need to mess with your OS installation for finding correct Python version and dependencies

# Supported Architectures
- amd64, arm

# Prerequisites

- Docker
- Raspberry PI (Optional)

# Generate API Key
- You should have your account id by looking to your browser address bar after logged in. URL should looks like this https://dash.cloudflare.com/<YOUR_ACCOUNT_ID>
- You can visit API token page by : https://dash.cloudflare.com/<YOUR_ACCOUNT_ID>/profile/api-tokens
- Create new a token with permission edit `Zone.DNS`
- Copy your token key and email for below step

# Usage

Using the command line

```cmd
$ docker run --name cloudflareddns -e CLOUDFLARE_APIKEY='YOUR APIKEY' -e CLOUDFLARE_EMAIL='YOUR EMAIL' -e DOMAINS='yourdomain1.com,yourdomain2.net' cuongtructran/py-cloudflare-ddns:latest 
```

Using the docker-compose:

```yaml
version: '3'
services:
  cloudflare-ddns:
    image: cuongtructran/py-cloudflare-ddns:develop
    environment:
      CLOUDFLARE_APIKEY: 'YOUR APIKEY'
      CLOUDFLARE_EMAIL: 'YOUR EMAIL'
      DOMAINS: 'yourdomain1.com,yourdomain2.net'
```

# Supported tags and respective Dockerfile links

- [1.0.0, latest](https://github.com/cuongtructran/cloudflare-ddns/blob/master/Dockerfile)

# CHANGELOG

Please visit CHANGELOG file in the repository for list of changes