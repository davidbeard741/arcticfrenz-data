```mermaid
graph TD
    style A fill:#004400,stroke:#b3c2bf,stroke-width:2px
    style B fill:#000088,stroke:#b3c2bf,stroke-width:2px
    style C fill:#004400,stroke:#b3c2bf,stroke-width:2px
    style D fill:#000088,stroke:#b3c2bf,stroke-width:2px
    style E fill:#004400,stroke:#b3c2bf,stroke-width:2px
    style F fill:#000088,stroke:#b3c2bf,stroke-width:2px
    style G fill:#004400,stroke:#b3c2bf,stroke-width:2px
    style H fill:#000088,stroke:#b3c2bf,stroke-width:2px
    style I fill:#880000,stroke:#b3c2bf,stroke-width:2px
    style J fill:#000088,stroke:#b3c2bf,stroke-width:2px
    style K fill:#880000,stroke:#b3c2bf,stroke-width:2px

    A[collection/with-rarity-and-holder-data.json] -->|Input| B(by-NFT_collection.py)
    B -->|Output| C[collection/by-NFT.json]
    C -->|Input| D(by-holder_collection.py)
    D -->|Output| E[collection/by-holder.json]
    E -->|Input| F(rank-holders_collection.py)
    F -->|Output| G[collection/ranked-holders.json]
    G -->|Input| H(top-holders_collection.py)
    H -->|Output| I[collection/top-holders.png]
    C -->|Input| J(histogram_collection.py)
    J -->|Output| K[collection/histogram.png]
