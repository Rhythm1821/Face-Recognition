# from flask import Flask, render_template,redirect

# app=Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("index.html")

# if __name__=="__main__":
#     app.run(debug=True)

from utils import *
# Main function
def main():
    cap = start_camera()
    root, camera_label = create_gui()

    def update():
        update_camera(cap, camera_label)
        root.after(10, update)

    update()
    root.mainloop()

if __name__ == "__main__":
    main()
