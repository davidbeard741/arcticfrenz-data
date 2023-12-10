```mermaid
graph LR
    style A fill:#556B2F,stroke:#4B5320,stroke-width:2px
    style B fill:#483D8B,stroke:#3B3C6D,stroke-width:2px
    style C fill:#2F4F4F,stroke:#264653,stroke-width:2px
    style D fill:#8B4513,stroke:#6E4B26,stroke-width:2px
    style E fill:#800000,stroke:#660000,stroke-width:2px
    style F fill:#4B0082,stroke:#3A0066,stroke-width:2px
    style G fill:#3C1414,stroke:#321010,stroke-width:2px
    style H fill:#003366,stroke:#002244,stroke-width:2px
    style I fill:#0B3D91,stroke:#07285F,stroke-width:2px
    style J fill:#1C352D,stroke:#142927,stroke-width:2px
    style K fill:#321414,stroke:#221010,stroke-width:2px

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
