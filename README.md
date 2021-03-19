# A simple hugo site for the DNM Bible

## Development server

1. [Install Hugo](https://gohugo.io/getting-started/installing/)
2. Clone this repository: `torsocks git clone http://thotstashp3v7yqih4b36yqjt7m756ydqfxpmrjfrk2n5xffse6p55ad.onion/Thotbot/hugo-bible.git`
3. `cd hugo-bible`
4. Start the server: `hugo server --minify --theme book`
5. Browse to http://127.0.0.1:1313

Changes made to the site's content will automatically update in the browser.

## Translations

### Adding a new language

1. In config.toml add the new language under \[languages\]
2. Add a new string translation file in `themes/book/i18n`
3. Create a new top-level directory named `content.<language_code>`
4. Copy the directory structure from `content` to the newly created directory
5. Begin translating the content

## How to host

### Using Nginx

1. [Install Hugo](https://gohugo.io/getting-started/installing/)
2. Install beautifulsoup4: `apt install python3-pip && pip3 install beautifulsoup4`
3. Generate the static site to the `./public` directory: `./generate.sh`
4. Copy the site from `./public/` to a directory accessible by nginx, for example `/usr/share/nginx/html`
5. Add a new server directive to your nginx config:

```
server {
    listen <portnumber>
    
    root /usr/share/nginx/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
    error_page 404 /404.html;
}
```
