import smtplib

hostName = 'smtp.gmail.com'
email = 'logeswaridillibabu96@gmail.com'
password1 = 'nhsglzfmeknhjrzm'

with smtplib.SMTP(host=hostName) as connection:
    connection.starttls()
    connection.login(user=email, password=password1)
    connection.sendmail(
        from_addr=email,
        to_addrs='nikhilkh1198@gmail.com',
        msg=f'Subject: Test python mail\n\n Hi Nikhil, This is a test mail'
    )