module.exports = (app) => {

    app.get("/", (req, res) => {
        return res.send("API is up and running!");
    });

    
}