def create_index_html(personal_id, output_fp):
    output_f = open(output_fp,'w')
    output_f.write('<html>')
    output_f.write('<head>')
    output_f.write('<title>Personal Microbiome Results: %s</title>' % personal_id)
    output_f.write('</head>')
    output_f.write('<body>')
    output_f.write('Subject %s: here are your personal microbiome results.' % personal_id)
    output_f.write('<hr>')
    output_f.write('Alpha rarefaction: alpha rarefaction measures ...<br>')
    output_f.write('''<a href="./alpha_rarefaction/rarefaction_plots.html">Open rarefaction plots</a>''')
    output_f.write('<hr>')
    output_f.write('Beta diversity: beta diversity shows... <br>')
    output_f.write('''<a href="./beta_diversity/unweighted_unifrac_pc_3D_PCoA_plots.html">Open beta diversity PCoA plots</a>''')
    output_f.write('<hr>')
    output_f.write('Thanks for participating in the study! Please direct any questions to ...')
    output_f.write('</body>')
    output_f.write('</html>')
    output_f.close()
    