from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

def ftoc(ftemp):
   return (ftemp - 32.0) * (5.0 / 9.0)

def ctof(ctemp):
   return (ctemp * (9.0 / 5.0) + 32.0)

def mtokm(mdis):
   return (mdis * 1.609)

def counter(a, b, c):
    count1 = a.count(b)
    count2 = b.count(c)
    return("Count 1: " + str(count1) + "\nCount 2: " + str(count2))
    
@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['ftemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', 
                               ftemp=ftemp_result, 
                               ctemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
    ftemp = 0.0
    try:
        ftemp = float(ftemp_str)
        ctemp = ftoc(ftemp)
        return "In Fahrenheit: " + ftemp_str + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftemp_str + " to a number"

@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')

@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['ctemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', 
                               ctemp=ctemp_result, 
                               ftemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ctof/<ctemp_str>')
def convert_ctof(ctemp_str):
    ctemp = 0.0
    try:
        ctemp = float(ctemp_str)
        ftemp = ctof(ctemp)
        return "In Fahrenheit: " + ctemp_str + " In Celsius " + str(ftemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ctemp_str + " to a number"

@app.route('/mtokm')
def render_mtokm():
    return render_template('mtokm.html')

@app.route('/mtokm_result')
def render_mtokm_result():
    try:
        mdis_result = float(request.args['mdis'])
        kmdis_result = mtokm(mdis_result)
        return render_template('mtokm_result.html', 
                               mdis=mdis_result, 
                               kmdis=kmdis_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/mtokm/<mdis_str>')
def convert_mtokm(mdis_str):
    mdis = 0.0
    try:
        mdis = float(mdis_str)
        kmdis = mtokm(mdis)
        return "In miles: " + mdis_str + " In kilometers " + str(kmdis) 
    except ValueError:
        return "Sorry.  Could not convert " + mdis_str + " to a number"

@app.route('/counting/<a>/<b>/<c>')
def counting(a, b, c):
    return(counter(a, b, c))

@app.route('/counting')
def render_counting():
    return render_template('counting.html')

@app.route('/counting_result')
def render_counting_result():
    try:
        string_a = request.args['string_a']
        string_b = request.args['string_b']
        string_c = request.args['string_c']
        result = counting(string_a, string_b, string_c)
        return render_template('counting_result.html', 
                               result = counter(string_a, string_b, string_c))
    except ValueError:
        return "Sorry: something went wrong."

if __name__ == "__main__":
   app.run(host='0.0.0.0')