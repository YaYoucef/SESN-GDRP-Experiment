# Use official BigchainDB base image
FROM bigchaindb/bigchaindb:2.0.0

# Set environment variables
ENV BIGCHAINDB_CONFIG_DIR=/bigchaindb
ENV BIGCHAINDB_DATABASE_NAME=bigchaindb

# Copy configuration files into the container
COPY bigchaindb_config.py $BIGCHAINDB_CONFIG_DIR/bigchaindb_config.py

# Expose default BigchainDB and Tendermint ports
EXPOSE 9984 26657 26656

# Initialize BigchainDB
RUN bigchaindb -y configure mongodb

# Start Tendermint and BigchainDB node
CMD tendermint node & bigchaindb start