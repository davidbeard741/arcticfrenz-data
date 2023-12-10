graph LR
    style A fill:#f9d5e5,stroke:#b388eb,stroke-width:2px
    style B fill:#f6cbd3,stroke:#f6cbd3,stroke-width:2px
    style C fill:#f9d5e5,stroke:#b388eb,stroke-width:2px
    style D fill:#f6cbd3,stroke:#f6cbd3,stroke-width:2px
    style E fill:#f9d5e5,stroke:#b388eb,stroke-width:2px
    style F fill:#f6cbd3,stroke:#f6cbd3,stroke-width:2px
    style G fill:#f9d5e5,stroke:#b388eb,stroke-width:2px
    style H fill:#f6cbd3,stroke:#f6cbd3,stroke-width:2px
    style I fill:#d5e4f1,stroke:#89c4f4,stroke-width:2px
    style J fill:#f6cbd3,stroke:#f6cbd3,stroke-width:2px
    style K fill:#d5e4f1,stroke:#89c4f4,stroke-width:2px

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
