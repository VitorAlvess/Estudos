//servidor

const express = require("express")
const server = express()

const { pageLanding, pageStudy, pageGiveClasses, saveClasses } = require("./pages")


//conf nunjucks (template engine)
const nunjucks = require("nunjucks")
nunjucks.configure("src/views", {
    express: server,
    noCache: true,
})
// inicio e conf do servidor
//configurar arquivos estaticos (css, script,image)
server
.use(express.urlencoded({extended: true}))
.use(express.static("public"))
//rotas da aplicação
.get("/", pageLanding)
.get("/study", pageStudy)
.get("/give-classes", pageGiveClasses)
.post("/save-classes", saveClasses)
.listen(5500)