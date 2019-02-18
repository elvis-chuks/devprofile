from flask import Flask, flash, request,render_template, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "superisasecretisakey"
##########################################################################################
#####################clears cache so that styling becomes easier##########################
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        #do something
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        fromaddr = request.form['email']

        toaddr = "celvischuks@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = request.form['subject']
        comnt = request.form['comment']
        body = "Hello elvis, \n {}, \n {}".format(comnt, fromaddr)
        html = """\
                <html>
                <head></head>
                <body>
                <h2>Hello elvis</h2>
                <p>i have reached you, please respond</p>
                   </body>
                   </html>
                   """
        part1 = MIMEText(body,'plain')
        part2 = MIMEText(html,'html')

        msg.attach(part1)
        msg.attach(part2)
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(toaddr, "@123elvischuks")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        flash('message sent')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, port="5000")