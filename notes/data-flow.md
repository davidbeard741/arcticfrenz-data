```mermaid
graph TD
    style A fill:#004400,stroke:#b3c2bf,stroke-width:2px  // .json
    style B fill:#000088,stroke:#b3c2bf,stroke-width:2px  // .py
    style C fill:#004400,stroke:#b3c2bf,stroke-width:2px  // .json
    style D fill:#000088,stroke:#b3c2bf,stroke-width:2px  // .py
    style E fill:#004400,stroke:#b3c2bf,stroke-width:2px  // .json
    style F fill:#000088,stroke:#b3c2bf,stroke-width:2px  // .py
    style G fill:#004400,stroke:#b3c2bf,stroke-width:2px  // .json
    style H fill:#000088,stroke:#b3c2bf,stroke-width:2px  // .py
    style I fill:#880000,stroke:#b3c2bf,stroke-width:2px  // .png
    style J fill:#000088,stroke:#b3c2bf,stroke-width:2px  // .py
    style K fill:#880000,stroke:#b3c2bf,stroke-width:2px  // .png

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
