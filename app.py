from Tool import app, db
import os
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for
from Tool.models import Urls


hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_data = Urls(og_url=request.form['url'])

        db.session.add(url_data)
        db.session.commit()

        if url_data is None:
            flash('URL is rquired!')
            return redirect(url_for('index'))

        url_id = url_data.id
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        url_data.short_url = short_url
        db.session.commit()

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/<id>')
def url_redirect(id):

    original_id = hashids.decode(id)

    if original_id:
        original_id = original_id[0]
        url_data = Urls.query.filter_by(id=original_id).first()
        print(url_data)
        og_url = url_data.og_url
        return redirect(og_url)
    else:
        flash('INVALID URL')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
