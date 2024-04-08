run tailwind css
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

run main
uvicorn main:app --reload
