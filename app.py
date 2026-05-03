from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello App</title>
  <style>
    :root {
      color-scheme: light;
      --bg: #f6f8fb;
      --panel: #ffffff;
      --text: #152033;
      --muted: #69758a;
      --accent: #0f766e;
      --accent-soft: #d9f4ef;
      --border: #dce3ec;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 24px;
      background:
        radial-gradient(circle at 15% 20%, rgba(15, 118, 110, 0.12), transparent 26%),
        linear-gradient(135deg, #f6f8fb 0%, #eef3f8 100%);
      color: var(--text);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    main {
      width: min(100%, 560px);
      padding: 44px;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.88);
      box-shadow: 0 24px 70px rgba(21, 32, 51, 0.12);
      text-align: center;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 22px;
      padding: 8px 12px;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--accent);
      font-size: 14px;
      font-weight: 700;
    }

    .badge::before {
      content: "";
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 0 5px rgba(15, 118, 110, 0.14);
    }

    h1 {
      margin: 0;
      font-size: clamp(52px, 14vw, 104px);
      line-height: 0.95;
      font-weight: 900;
      letter-spacing: 0;
    }

    p {
      margin: 20px auto 0;
      max-width: 34rem;
      color: var(--muted);
      font-size: 18px;
      line-height: 1.6;
    }

    @media (max-width: 520px) {
      main {
        padding: 34px 22px;
      }

      p {
        font-size: 16px;
      }
    }
  </style>
</head>
<body>
  <main>
    <div class="badge">Python HTTP server</div>
    <h1>HELLO</h1>
    <p>A simple local app running on port 5001.</p>
  </main>
</body>
</html>
""".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = HTTPServer(("0.0.0.0", 5001), HelloHandler)
    print("Serving HELLO on http://0.0.0.0:5001")
    server.serve_forever()


if __name__ == "__main__":
    main()
