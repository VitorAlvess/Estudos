const Database = require('./db');
const createProffy = require('./createProffy')

Database.then(async (db) => {
   //inserir dados 
  proffyValue = {
    name: "Creuza",
    avatar: "https://i.pinimg.com/originals/8b/da/ca/8bdaca81d5ddbaeb92b61d6b5787d866.jpg",
    whatsapp: 99123456789,
    bio: "ela faz os bagulho ae",
  }
  classValue = {
    subject: 10, 
    cost: "500", 
  }
   //proffy id vira pelo banco de dados
  classScheduleValues = [
     //class_id id vira pelo banco de dados
    {
      weekday: 1,
      time_from: 1200,
      time_to: 1800
    },
    {
      weekday: 0,
      time_from: 520,
      time_to: 1220
    }
  ]

  const selectedProffys = await db.all("SELECT * FROM proffys")

    //consultar as classes de um determinado professor e trazer junto os dados dele

  const selectClassesAndProffys = await db.all(`
    SELECT classes.*, proffys.*
    FROM proffys
    JOIN classes ON (classes.proffy_id = proffys.id)
    WHERE classes.proffy_id = 1;
  `)

   //Filtro dsa horas ><
  const selectClassesSchedules = await db.all(`
    SELECT class_schedule.*
    FROM class_schedule
    WHERE class_schedule.class_id = "1"
    AND class_schedule.weekday = "0"
    AND class_schedule.time_from <= "520"
    AND class_schedule.time_to > "520"
  `)
})