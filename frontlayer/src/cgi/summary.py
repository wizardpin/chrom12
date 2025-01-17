#!/usr/bin/env python

"""*************************************************************************************************
* project: Genome browse for chromosome-12                                                         *
* file:get_result.py                                                                               *
* Date: 08/05/2018                                                                                 *
* version:v1.0                                                                                     *
* Function : This python script generate result page according to user input in search             *                                         *
* Licence:See the LICENSE.txt for licensing information                                            *
* Author: Abdulvahab Kharadi                                                                       *
* ***********************************************************************************************"""

from middlelayer import vari
import json
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html\n")

def result():
    result = json.loads(vari())
    return result
def html():
    html ='<html lang="en">'
    html += '<head>'
    html += "<title>Chromosome-12 Information</title>"
    html += "<meta charset='utf-8'>"
    html += "<meta name='viewport' content='width=device-width,initial-scale=1.0'>"
    html += '<link rel ="stylesheet" type="text/css" href = "http://localhost/chrom12/frontlayer/src/html/main.css">'
    #html += '<link rel="stylesheet" href="https://localhost/chrom12/frontlayer/src/html/main.css">'
    html += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
    html += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>'
    html += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
    html += "<style>"
    html += '''body{
    color:#660099;
    text-align: center;
    background-size:cover;
    background-color: rgba(255,255,255,0.7);
    background-blend-mode: lighten;
    background-image: url('http://localhost/chrom12/frontlayer/src/img/chromo1.jpg');
    background-repeat: no-repeat;
    margin-bottom:50px;
    }'''
    html += "</style>"
    html += '</head>'
    html += "<div class='main-container'>"
    html += "<header ><h1>Summary of Chromosome 12</h1></header>"
    html += '<nav>'
    html += "<a href='http://localhost/chrom12/frontlayer/src/html/index.html'>Home  |</a>"
    html += "<a href='http://localhost/cgi-bin/summary.py'>Summary  |</a>"
    html += "<a href='http://localhost/chrom12/frontlayer/src/html/contactus.html'>Contact us  </a>"
    html += '</nav>'
    html += "<div class='footer'>&copy; 2018,Group Chromosome-12.</div>"
    html += '<div>'
    html += "<table class=table table-condensed >"
    html += "<thead>"
    html += "<tr>"
    html += "<th>Gene Identifires</th>"
    html += "<th>Genebank Accssion</th>"
    html += '<th>Protein Product</th>'
    html += '<th>Chromosomal Location</th>'
    html += '</tr>'
    html += '</thead>'
    for i in range(len(result())):
        html += '<tr style=text-align:center;>'
        html += "<th id='gene_id'>{}</th>".format(result()['gene_id'][i])
        html += "<th id='acc_num'>{}</th>".format(result()['acc_num'][i])
        html += "<th id='protein'>{}</th>".format(result()['protein'][i])
        html += "<th id='chromo_location'>{}</th>".format(result()['chromo_location'][i])
        html += '</tr>'
    html += '</tbody>'
    html += '</table>'
    html += '<div>'
    html += '<script>'
    html += '</body>'
    html += '</html>'
    print(html)
if __name__=="__main__":
    html()
