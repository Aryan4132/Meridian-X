# 🌐 Meridian-X Server Setup & Self-Hosting Guide

Complete step-by-step guide for hosting the **Meridian-X** backend daemon on a VPS, home server, or cloud instance (Ubuntu, Debian, macOS, or Windows Server) and connecting remote desktop/web clients securely.

---

## 📋 Prerequisites

- **Host Machine**: VPS / Cloud Instance (2+ CPU Cores, 4+ GB RAM, Docker installed)
- **Software**: Docker & Docker Compose
- **Optional**: Custom domain name pointing to your server IP for HTTPS SSL certificates

---

## 🛠️ Step 1: Download Deployment Files

Clone the repository or download `docker-compose.yml` directly onto your server:

```bash
mkdir meridian-server && cd meridian-server
curl -fsSL https://raw.githubusercontent.com/Aryan4132/Meridian-X/main/docker-compose.yml -o docker-compose.yml
```

---

## ⚙️ Step 2: Configure Environment Variables

Create `.env` file in the same directory:

```env
# Server Configuration
HOST=0.0.0.0
PORT=4132

# Security & API Key
AUTH_ENABLED=true
MERIDIAN_API_KEY=my_super_secret_secure_key_12345

# Ollama Engine Connection
OLLAMA_HOST=http://ollama:11434
MERIDIAN_MODEL=llama3.2:3b
DOMAIN=api.your-domain.com
```

---

## 🚀 Step 3: Launch Docker Stack

Run the stack in detached background mode:

```bash
docker compose up -d
```

Verify running containers:

```bash
docker compose ps
```

- Backend container: `meridian-backend` (listening on port `4132`)
- Ollama container: `meridian-ollama` (listening on port `11434`)

---

## 🧠 Step 4: Download AI Models on Server

Pull your preferred offline LLM model into the server's Ollama instance:

```bash
# Recommended for standard servers (8 GB RAM)
docker exec -it meridian-ollama ollama pull llama3.2:3b

# Optional: Pull lightweight model for budget VPS (2–4 GB RAM)
docker exec -it meridian-ollama ollama pull llama3.2:1b
```

---

## 🔒 Step 5: HTTPS SSL Setup via Reverse Proxy

To connect securely over the public internet, configure Caddy or Nginx for automatic HTTPS SSL termination.

### Option A: Automatic SSL via Caddy (Recommended)

Create `Caddyfile`:

```text
api.your-domain.com {
    reverse_proxy 127.0.0.1:4132
}
```

Run Caddy:

```bash
caddy run --config Caddyfile
```

### Option B: Using Nginx + Certbot (Let's Encrypt)

Create `/etc/nginx/sites-available/meridian.conf`:

```nginx
server {
    server_name api.your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:4132;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable configuration and issue SSL certificate:

```bash
sudo ln -s /etc/nginx/sites-available/meridian.conf /etc/nginx/sites-enabled/
sudo systemctl reload nginx
sudo certbot --nginx -d api.your-domain.com
```

### Option C: 1-Command Production Docker Stack (with Caddy SSL Container)

Use `docker-compose.prod.yml`:

```bash
docker compose -f docker-compose.prod.yml up -d
```

---

## 🖥️ Step 6: Connect Desktop / Web Frontend Client

1. Open **Meridian-X Desktop App** or **Web Interface**.
2. Go to **Settings** -> Click **Backend Server Settings** (or click the 🌐 icon).
3. Set **Server URL**: `https://api.your-domain.com` (or `http://YOUR_SERVER_IP:4132`).
4. Set **API Key**: Enter the secret key configured in step 2 (`my_super_secret_secure_key_12345`).
5. Click **Test Connection** -> Verify **"✅ Connected successfully!"**.
6. Click **Save & Connect**.

---

## 🔍 Health Check & Debugging

- **Test API Status**: `curl http://YOUR_SERVER_IP:4132/api/health`
- **Inspect Backend Logs**: `docker compose logs -f meridian-backend`
- **Inspect Ollama Logs**: `docker compose logs -f ollama`
