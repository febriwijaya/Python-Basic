from flask import Flask, render_template, request, session
from author_book import author_book

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKeyKu2021"


@app.route("/")
def indexku():
  # Belajar looping
  hari = ['senin','selasa', 'rabu', 'kamis', 'jumat','sabtu', 'minggu']
  # belajar conditional
  suasana = "sedih"
  return render_template("index.html", value=hari, suasana=suasana)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/about")
def about():
  return render_template("about.html")

# parsing nilai int, string
@app.route("/parsing/<int:nilaiku>")
def parsing(nilaiku):
  return "nilainya adalah : {}".format(nilaiku)

# argumen parser
@app.route("/parsingargument")
def parsingargument():
  data = request.args.get("nilai")
  return "nilainya dari argument parser adalah {}".format(data)

# memparsing nilai dari url untuk mengeset nilai session
@app.route("/halaman/<int:nilai>")
def session_1(nilai):
  session["nilaiku"] = nilai
  return "Berhasil mengeset nilainya"

@app.route("/halaman/lihat")
def view_session_1():
  try:
    data = session["nilaiku"]
    return "Nilai yang telah diset adalah = {}".format(data)
  except:
    return "Anda tidak memiliki nilai session lagi"
    
# logout / destroy session
@app.route("/halaman/logout")
def logout():
  session.pop("nilaiku")
  return "Berhasil logout / menghapus session"

@app.route('/author', methods=['GET', 'POST'])
def author():
  if 'author_id' in request.form:
    author_book[request.form['author_id']] = []
    
  return render_template('author.html', author_book = author_book)

if __name__ == "__main__":
  app.run(debug=True)