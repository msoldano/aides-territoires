const express = require("express");
const graphqlHTTP = require("express-graphql");
const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/aides-territoires");

// middleware express pour ajouter les headers CORS
const cors = require("cors");
const graphql = require("graphql");
const { buildSchema, GraphQLSchema } = require("graphql");

const helloWorldGraphqlSchema = require("./services/helloWorld/graphql/helloWorldGraphqlSchema");
const aideGraphqlSchema = require("./services/aide/graphql/aideGraphqlSchema");

// our full graphQL schema
const schema = new graphql.GraphQLSchema({
  // "query" type contains all our queries types
  query: new graphql.GraphQLObjectType({
    name: "Query",
    fields: {
      helloWorld: helloWorldGraphqlSchema.query,
      aideGet: aideGraphqlSchema.query
    }
  }),
  // "mutation" type contains all our mutations types
  mutation: new graphql.GraphQLObjectType({
    name: "Mutation",
    fields: {
      aideSave: aideGraphqlSchema.mutation
    }
  })
});

const isDev = process.env.NODE_ENV === "development";
const app = express();
app.use(cors());

app.use(
  "/graphql",
  graphqlHTTP({
    schema,
    rootValue: root,
    // always display graphiql explorer for now
    graphiql: true
  })
);

app.use("/", (req, res) => {
  res.json("Go to /graphql to test your queries and mutations!");
});

app.listen(4000);
console.log("Running a GraphQL API server at localhost:4000/graphql");
