```mermaid
graph TD
    style A fill:#1a1e21,stroke:#b3c2bf,stroke-width:2px
    style B fill:#1a2025,stroke:#b3c2bf,stroke-width:2px
    style C fill:#1a2329,stroke:#b3c2bf,stroke-width:2px
    style D fill:#1a262d,stroke:#b3c2bf,stroke-width:2px
    style E fill:#1a2931,stroke:#b3c2bf,stroke-width:2px
    style F fill:#1a2c35,stroke:#b3c2bf,stroke-width:2px
    style G fill:#1a2f39,stroke:#b3c2bf,stroke-width:2px
    style H fill:#1a323d,stroke:#b3c2bf,stroke-width:2px
    style I fill:#1a3541,stroke:#b3c2bf,stroke-width:2px
    style J fill:#1a3845,stroke:#b3c2bf,stroke-width:2px
    style K fill:#1a3b49,stroke:#b3c2bf,stroke-width:2px

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
