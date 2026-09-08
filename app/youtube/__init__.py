from Flask import Blueprint , request , jsonify

youtube_bp = Blueprint(
  "youtube",
  __name__
  }

@youtube_bp.route(
  "/play" ,
  method =["POST"]

  )
  def play ():

  data= request.get_json(
  silent = true
  )or {}

  command = data.get(
  "command"
  ""
  ).strip()
if not command :

  return jsonify({
    "success":"false",
    "message":"there's no song name , mentioned "
  )}



  
