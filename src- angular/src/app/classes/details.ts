export class details
{
    constructor(
                public id:number=0,
                public name:string="",
                public lastName:string="",
                public mail:string="", 
                public password:string="",
                public a:string="",
                public age:number=0, 
                public gender:number=0, 
                public kg:number=0, 
                public high:number=0, 
                public bloodGlucoseLevel:number=0, 
                public hba1cLevel:number=0,
                public smokingHistory:number=0, 
                public heartDisease:boolean=false, 
                public hypertension:boolean=false)
    {}
    // gender:
    // 1- גבר
    // 2- אישה

    // smokingHistory:
    // 1- No Info - אין מידע
    // 2- never - אף פעם
    // 3- ever - אי פעם
    // 4- former - בעבר
    // 5- current - נוכחי
}