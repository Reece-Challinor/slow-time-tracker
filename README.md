

graph TD
    A[Initial Setup] --> B[Life Expectancy Calculator]
    B --> C[Time Allocation Engine]
    C --> D[Visualization Generator]
    D --> E[Static Site Generator]
    E --> F[S3 Hosting]
    
    subgraph "Setup Flow"
    A --> |User Inputs| G[Demographics Form]
    G --> |Health Factors| H[Location Data]
    H --> |Lifestyle| I[Work/Sleep Pattern]
    end
    
    subgraph "Visualization Types"
    D --> J[ASCII Dot Matrix]
    D --> K[ASCII Bar Graph]
    D --> L[ASCII Histogram]
    end
    
    subgraph "Build Process"
    M[GitHub Action] --> |Triggers| N[Daily Build]
    N --> |Updates| E
    end