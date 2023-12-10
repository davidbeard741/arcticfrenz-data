```mermaid
graph TD
    style A fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style B fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style C fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style D fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style E fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style F fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style G fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style H fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style I fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style J fill:#343a40,stroke:#b3c2bf,stroke-width:2px
    style K fill:#343a40,stroke:#b3c2bf,stroke-width:2px

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
