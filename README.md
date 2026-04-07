usecaseDiagram
    actor User as "System User"
    actor API as "NBP API"

    package "Currency Exchange Analyzer" {
        usecase UC1 as "Select Parameters (Currency, Time Period, Analysis Type)"
        usecase UC2 as "Calculate Session Trends (Growth, Drop, No-change)"
        usecase UC3 as "Calculate Statistical Measures (Median, Mode, SD, CV)"
        usecase UC4 as "Generate Change Distribution Histogram"
        usecase UC5 as "Fetch Exchange Rate Data"
        usecase UC6 as "Display Results in Console"
    }

    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC6

    UC2 ..> UC5 : <<include>>
    UC3 ..> UC5 : <<include>>
    UC4 ..> UC5 : <<include>>

    UC5 <-- API
