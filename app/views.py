from app import app
from flask import render_template, redirect, flash, request, Response
from app.forms import EndpointForm
from app.models import Endpoint

import time

@app.route('/', methods=['GET', 'POST'])
def index():
  print 'Index called'
  form = EndpointForm(request.form)

  if form.validate_on_submit():
    endpoint = Endpoint()
    form.populate_obj(endpoint)

    endpoint.save()
    flash('Endpoint saved successfully!')

    return redirect('/')

  return render_template('index.html', title='Create an Endpoint', form=form)



@app.route('/<path:path>')
def catchall(path):
  print 'Catcch all called with {0}'.format(path)
  endpoint = Endpoint.objects.get_or_404(path=path)

  if endpoint.latency:
    time.sleep(endpoint.latency)

  return Response('', status=endpoint.status_code, mimetype=endpoint.content_type)