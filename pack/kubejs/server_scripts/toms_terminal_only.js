ServerEvents.recipes(event => {
  const disabledRecipes = [
    'toms_storage:basic_inventory_hopper',
    'toms_storage:filing_cabinet',
    'toms_storage:inventory_cable_connector_framed',
    'toms_storage:inventory_cable_connector_framed_clean',
    'toms_storage:inventory_cable_framed',
    'toms_storage:inventory_cable_framed_clean',
    'toms_storage:inventory_configurator',
    'toms_storage:inventory_interface',
    'toms_storage:inventory_proxy',
    'toms_storage:inventory_proxy_clean',
    'toms_storage:item_filter',
    'toms_storage:level_emitter',
    'toms_storage:open_crate',
    'toms_storage:paint_kit',
    'toms_storage:poly_item_filter',
    'toms_storage:tag_item_filter',
    'toms_storage:trim',
    'toms_storage:trim_clean'
  ]

  disabledRecipes.forEach(id => event.remove({ id: id }))
})
