import re
from urllib.parse import urlparse

def extract_features(url):
    try:
        if not str(url).startswith(('http://', 'https://')):
            url_parsed = urlparse('http://' + str(url))
        else:
            url_parsed = urlparse(str(url))
        
        domain = url_parsed.netloc
        path = url_parsed.path
    except Exception:
        domain = str(url)
        path = ""

    url_str = str(url)

    # 1. URL Length
    url_length = len(url_str)
    
    # 2. Has @ symbol
    has_at = 1 if '@' in url_str else 0
    
    # 3. Has IP address
    ip_pattern = r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-5])'
    has_ip = 1 if re.search(ip_pattern, domain) else 0
    
    # 4. Subdomain count
    dots = domain.count('.')
    subdomain_count = dots - 1 if dots > 1 else 0
    
    # 5. Path depth
    path_depth = len([p for p in path.split('/') if p])
    
    # 6. Suspicious keywords
    keywords = ['login', 'signin', 'bank', 'account', 'update', 'verify', 'secure', 'ebayisapi', 'paypal']
    has_keyword = 1 if any(kw in url_str.lower() for kw in keywords) else 0
    
    # 7. Is HTTPS
    is_https = 1 if url_str.startswith('https://') else 0
    
    # 8. Has hyphen in domain
    has_hyphen = 1 if '-' in domain else 0
    
    # 9. URL shortener
    shorteners = ['bit.ly', 'goo.gl', 'tinyurl', 't.co', 'is.gd', 'cli.gs']
    has_shortener = 1 if any(s in domain for s in shorteners) else 0
    
    # 10. Domain length
    domain_length = len(domain)

    return [
        url_length, has_at, has_ip, subdomain_count,
        path_depth, has_keyword, is_https,
        has_hyphen, has_shortener, domain_length
    ]