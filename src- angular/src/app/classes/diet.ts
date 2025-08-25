export class diet
{
    constructor
    (
        public id:number=0,
        public chanceDiabetes:number=0,
        public sunday:Array<Array<string>>=new Array(),
        public monday:Array<Array<string>>=new Array(),
        public tuesday:Array<Array<string>>=new Array(),
        public wednesday:Array<Array<string>>=new Array(),
        public thursday:Array<Array<string>>=new Array(),
        public friday:Array<Array<string>>=new Array(),
        public saturday:Array<Array<string>>=new Array(),
    )
    {}
    

}