```mermaid
graph LR
    A[nft_metadata_with_rarity_and_holder_data.json] -->|Input| B(by-NFT)
    B -->|Output| C[by-NFT.json]
    C -->|Input| D(by-holder)
    D -->|Output| E[by-holder.json]
    E -->|Input| F(rank-holders)
    F -->|Output| G[ranked-holders.json]
    G -->|Input| H(top-holders)
    H -->|Output| I[top-holders.png]
    C -->|Input| J(histogram)
    J -->|Output| K[histogram.png]
