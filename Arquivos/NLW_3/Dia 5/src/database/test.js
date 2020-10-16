const Database = require('./db')
const saveOrphanage = require('./saveOrphanage')
Database.then(async db =>{
    //inserir dados na tabela
    await saveOrphanage(db, {
        
        lat: "-23.5707501",
        lng: "-46.6410928",
        name: "Lar da meninas",
        about: "Orfanato lar das meninas, venha conhecer",
        whatsapp: '113458140604',
        images:[
            "https://images.unsplash.com/photo-1595207011175-3d72f5a3b21c?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjF9",

            "https://images.unsplash.com/photo-1600711725042-deb9fbaeb1e3?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjF9"
        ].toString(),
        instructions: "Venha tal tal tal tal tal tal ",
        opening_hours: " Horario de visitas 18 ate 8hrs",
        open_on_weekends: "1"

    })
    //consultar
    const selectedOrphanages = await db.all("SELECT * FROM orphanages")
     console.log(selectedOrphanages);

    const orphanage = await db.all('SELECT * FROM orphanages WHERE id = "2" ')
    console.log(orphanage);

    // Apagar uma tabela (informar o id)console.log(await db.run("DELETE FROM orphanages WHERE id = ''"))
})