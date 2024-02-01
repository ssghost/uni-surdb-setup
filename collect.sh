cryo logs \
    --label uniswap_v3_pools \
    --blocks -10000:latest \
    --reorg-buffer 1000 \
    --subdirs datatype \
    --contract 0x1f98431c8ad98523631ae4a59f267346ea31f984 \
    --event-signature "PoolCreated(address indexed token0, address indexed token1, uint24 indexed fee, int24 tickSpacing, address pool)" \
    --topic0 0x783cca1c0412dd0d695e784568c96da2e9c22ff989357a2e8b1d9b2b4e6b7118 \
    --rpc $RPC_URL \
    --json
