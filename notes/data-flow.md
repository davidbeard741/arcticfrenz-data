```mermaid
graph LR
    style A fill:#f9d5e5,stroke:#b3c2bf,stroke-width:2px
    style B fill:#eeac99,stroke:#b3c2bf,stroke-width:2px
    style C fill:#f6dfeb,stroke:#b3c2bf,stroke-width:2px
    style D fill:#d5e1df,stroke:#b3c2bf,stroke-width:2px
    style E fill:#e3eaa7,stroke:#b3c2bf,stroke-width:2px
    style F fill:#b5e7a0,stroke:#b3c2bf,stroke-width:2px
    style G fill:#86af49,stroke:#b3c2bf,stroke-width:2px
    style H fill:#405d27,stroke:#b3c2bf,stroke-width:2px
    style I fill:#f7cac9,stroke:#b3c2bf,stroke-width:2px
    style J fill:#92a8d1,stroke:#b3c2bf,stroke-width:2px
    style K fill:#034f84,stroke:#b3c2bf,stroke-width:2px

    A[nft_metadata_with_rarity_and_holder_data.json] -->|Input| B(by-NFT.py)
    B -->|Output| C[by-NFT.json]
    C -->|Input| D(by-holder.py)
    D -->|Output| E[by-holder.json]
    E -->|Input| F(rank-holders.py)
    F -->|Output| G[ranked-holders.json]
    G -->|Input| H(top-holders.py)
    H -->|Output| I[top-holders.png]
    C -->|Input| J(histogram.py)
    J -->|Output| K[histogram.png]
