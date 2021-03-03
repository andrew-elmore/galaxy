const huntrFunc = (activities) => {
    document.querySelector('#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(1) > div > div:nth-child(2) > a').click()
    activities.forEach( activity => {
        let activityNumber = 0
        switch (activity.type) {
            case 'DS&A':
                activityNumber = 1
                break;
            case 'Coding':
                activityNumber = 7
                break;
            case 'Studying':
                activityNumber = 3
                break;
            case 'Pairboarding':
                activityNumber = 4
                break;
        
            default:
                break;
        }

        let activityNumber = 1
        let week = 1
        let day = 'today'
        let startTime = 5
        let endTime = 6
        document.querySelector('#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(1) > div > div:nth-child(2) > a').click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(${activityNumber}) > div > p`).click()
        document.querySelector('#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div > div > p').click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div.react-datepicker__tab-loop > div.react-datepicker-popper.huntr-date-picker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(${week}) > div.react-datepicker__day.react-datepicker__day--00${day}`).click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > div.react-datepicker__tab-loop > div.react-datepicker-popper.huntr-date-picker-popper > div > div > div.react-datepicker__time-container.react-datepicker__time-container--with-today-button > div.react-datepicker__time > div > ul > li:nth-child(${startTime})`).click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div > div > p`).click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div.react-datepicker__tab-loop > div.react-datepicker-popper.huntr-date-picker-popper > div > div > div.react-datepicker__month-container > div.react-datepicker__month > div:nth-child(${week}) > div.react-datepicker__day.react-datepicker__day--00${day}`).click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div.react-datepicker__tab-loop > div.react-datepicker-popper.huntr-date-picker-popper > div > div > div.react-datepicker__time-container.react-datepicker__time-container--with-today-button > div.react-datepicker__time > div > ul > li:nth-child(${endTime})`).click()
        document.querySelector(`#react-container > div > div > div:nth-child(3) > div.rmq-585afbed.rmq-bab34353.rmq-10f184ee.rmq-a71eaf84.rmq-a2af41ab.rmq-84c71bea.transparent-scrollbar > div > div > div > div > div > div.rmq-c871bfa8.transparent-scrollbar > div > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(3) > a:nth-child(2)`).click()
        
    })

}

