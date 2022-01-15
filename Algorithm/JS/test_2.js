function solution(){
    var answer = -1;
    
    // if(birth.length !== 10){
    //   return null
    // }
    birth.map(date => dateFormat(date));

    function dateFormat(date) {
      const formattedDate = new Date(date);
      const year = formattedDate.getFullYear();
      console.log('year', year);
      if(year >= 1900 &&  year<= 2021){
        console.log('date', date);
      }
      return null
    }
    
    return answer;
}



const birth = [
  '1899-13-31',
  '19001231',
  '2001-09-04',
  '1900-02-29',
  '2021-5-31',
  '1950-11-30',
  '1996-02-29',
  '1999-11-31',
  '2000-02-29',
];

solution(birth);