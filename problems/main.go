package main

import (
	"bufio"
	"database/sql"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	_ "github.com/go-sql-driver/mysql"
)

var db *sql.DB

func main() {
	dsn := "root:example@tcp(:3306)/gofactor?timeout=90s&charset=utf8mb4&collation=utf8mb4_unicode_ci&parseTime=true"

	initDB := flag.Bool("init-db", false, "initialize db")
	flag.Parse()

	var err error

	if *initDB {
		println("Initializing database ..")
		db, err = sql.Open("mysql", strings.Replace(dsn, "/gofactor", "/", 1))
		if err != nil {
			panic(err)
		}
		defer db.Close()

		_, err = db.Exec("DROP DATABASE IF EXISTS gofactor")
		if err != nil {
			panic(err)
		}
		_, err = db.Exec("CREATE DATABASE gofactor")
		if err != nil {
			panic(err)
		}
		_, err = db.Exec(`
		CREATE TABLE gofactor.users (
			id INT AUTO_INCREMENT PRIMARY KEY,
			email VARCHAR(20),
			name VARCHAR(20),
			password VARCHAR(20),
			created_at TIMESTAMP NULL,
			updated_at TIMESTAMP NULL
		)`)
		if err != nil {
			panic(err)
		}
		println("Done.")
		os.Exit(0)
	}

	println("Connecting to database ..")
	db, err = sql.Open("mysql", dsn)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	println("Pinging database ..")
	err = db.Ping()
	if err != nil {
		panic(err)
	}

	http.HandleFunc("/", root)
	http.HandleFunc("/user", user)
	http.HandleFunc("/latest-reviews", latestReviews)

	println("Server listening on port 8090")
	http.ListenAndServe(":8090", nil)
}

func user(w http.ResponseWriter, req *http.Request) {
	switch req.Method {

	case "POST":
		buf := make([]byte, req.ContentLength)
		_, err := io.ReadFull(req.Body, buf)
		if err != nil {
			panic(err)
		}
		payload := struct {
			Email    string
			Name     string
			Password string
		}{}
		err = json.Unmarshal(buf, &payload)
		if err != nil {
			panic(err)
		}
		r, err := db.Exec("INSERT INTO gofactor.users SET email = ?, name = ?, password = ?", payload.Email, payload.Name, payload.Password)
		if err != nil {
			panic(err)
		}
		lastID, _ := r.LastInsertId()
		println(fmt.Sprintf("Created new user: %d", lastID))

	case "GET":
		idParam := req.URL.Query().Get("id")
		if idParam == "" {
			panic("Missing id query param")
		}
		id, _ := strconv.ParseInt(idParam, 10, 32)
		println(fmt.Sprintf("Fetching user: %d", id))
		r, err := db.Query("SELECT * FROM gofactor.users WHERE id = ?", id)
		if err != nil {
			panic(err)
		}
		defer r.Close()
		if r.Next() {
			var id int
			var email string
			var name string
			var password string
			var createdAt sql.NullTime
			var updatedAt sql.NullTime
			err = r.Scan(&id, &email, &name, &password, &createdAt, &updatedAt)
			if err != nil {
				panic(err)
			}
			println(fmt.Sprintf("Found user: %d", id))
			fmt.Fprintf(w,
				"id=%d\n"+
					"email=%s\n"+
					"name=%s\n"+
					"password=%s\n"+
					"created_at=%s\n"+
					"updated_at=%v\n",
				id, email, name, password, createdAt.Time.Local(), updatedAt.Time.Local())
			return
		}

	case "PATCH":
		buf := make([]byte, req.ContentLength)
		_, err := io.ReadFull(req.Body, buf)
		if err != nil {
			panic(err)
		}
		payload := struct {
			ID       int
			Email    string
			Name     string
			Password string
		}{}

		err = json.Unmarshal(buf, &payload)
		if err != nil {
			panic(err)
		}
		println(fmt.Sprintf("Updating user: %d", payload.ID))
		r, err := db.Exec("UPDATE gofactor.users SET email = ?, name = ?, password = ? WHERE id = ?", payload.Email, payload.Name, payload.Password, payload.ID)
		if err != nil {
			panic(err)
		}
		rows, _ := r.RowsAffected()
		println(fmt.Sprintf("Updated user: %d (%d rows)", payload.ID, rows))
	}

	fmt.Fprintf(w, "OK\n")
}

var handlerCallCounter int

func latestReviews(w http.ResponseWriter, req *http.Request) {
	println("Fetching latest reviews ..")
	resp, err := http.Get("https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=&api-key=1ODRGmfb2AOQGeKCuwZXqik6LCfrSIHh")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	println("Response status:", resp.Status)
	var lines []string
	scanner := bufio.NewScanner(resp.Body)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
	println(fmt.Sprintf("Scanned %d lines", len(lines)))
	data := map[string]interface{}{}
	err = json.Unmarshal([]byte(strings.Join(lines, "")), &data)
	if err != nil {
		panic(err)
	}
	pretty, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		panic(err)
	}
	println(fmt.Sprintf("Created %d bytes of pretty JSON", len(pretty)))
	handlerCallCounter++
	println(fmt.Sprintf("Total calls to this handler: %d", handlerCallCounter))
	fmt.Fprint(w, string(pretty))
}

func root(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "hello, it's %s\n", time.Now())
}


{
    "first_name": "Prashu",
    "last_name": "Chaudhary",
    "username": "prashuChaudhary",
    "email": "prashu@google.com",
    "password": "dafdfas"
}


